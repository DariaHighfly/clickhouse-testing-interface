<template>
    <div class="column-chart">
        <p class="column-chart__title">TIME PERFORMANCE OF All TESTS' QUERIES</p>
        <div class="params">
            <div class="params_box">
                <p class="params__title">
                    Minimum Threshold (abs):
                </p>
                <div class="params__input-box">
                    <button class="params__input-box__button button-left" v-on:click="changeThreshold(0)">-</button>
                    <input class="params__input-box__input" type="number" v-model="minimumThreshold" :min="0" :max="10000" step="0.01">
                    <button class="params__input-box__button button-right" v-on:click="changeThreshold(1)">+</button>
                </div>
            </div>
            <div class="params_box">
                <p class="params__title">
                    Percentile:
                </p>
                <div class="params__radio">
                    <div class="params__radio_column" v-for="value in Object.keys(criticalValues)">
                        <input type="radio" :id="value" :value="value" v-model="picked">
                        <label :for="value">{{value}} %</label>
                    </div>
                </div>
            </div>
        </div>
        <highcharts :options="timeColumnChartOptions"></highcharts>
    </div>
</template>

<script>
    export default {
        name: "TimePerformanceAllQueries",
        props: {
            timePerformance: {
                type: Object,
                default: {}
            }
        },
        data() {
            return {
                testNames: [],
                minimumThreshold: 0.06,
                picked: 5,
                criticalValues: {
                    5: 0.65,
                    50: 0.68,
                    95: 1.96,
                    99: 2.58
                },
            }
        },
        computed: {
            testNamesForChart() {
                return this.testNames;
            },
            series() {

                // Variant without minus 1

                // let data = [];
                // let avgTime = [];
                // let points = [];
                // for (let key in this.timePerformance) {
                //     // Average of time difference
                //     for (let i = 0; i !== this.timePerformance[key].length; ++i) {
                //         let ratio = [];
                //         for (let j = 0; j !== this.timePerformance[key][i].newTime.length; ++j) {
                //             ratio.push(this.timePerformance[key][i].oldTime[j] / this.timePerformance[key][i].newTime[j]);
                //         }
                //         let avg = Math.pow(ratio.reduce((result, currentRatio) => {
                //             return result *= currentRatio}), 1/ratio.length);
                //         if (avg < 1) {
                //             if (Math.abs(-1/avg) > this.minimumThreshold) {
                //                 data.push({ name: key, value: -1/avg, points: ratio.map(elem => -elem)});
                //             }
                //         } else {
                //             if (avg > this.minimumThreshold) {
                //                 data.push({ name: key, value: avg, points: ratio});
                //             }
                //         }
                //     }
                // }
                // data.sort((a, b) => {
                //     return (a.value - b.value);
                // });
                // data.map(elem => avgTime.push(parseFloat(elem.value)).toFixed(4));
                // data.map(elem => {
                //     // console.log([Math.min(...elem.points), Math.max(...elem.points)]);
                //     points.push([Math.min(...elem.points), Math.max(...elem.points)])
                // });
                // // console.log(points);
                // this.testNames = [];
                // data.map(elem => this.testNames.push(elem.name));

                // Variant with minus 1

                let data = [];
                let avgTime = [];
                let points = [];
                let errorIntervals = [];
                for (let key in this.timePerformance) {
                    // Average of time difference
                    for (let i = 0; i !== this.timePerformance[key].length; ++i) {
                        let ratio = [];
                        for (let j = 0; j !== this.timePerformance[key][i].newTime.length; ++j) {
                            ratio.push(this.timePerformance[key][i].newTime[j] / this.timePerformance[key][i].oldTime[j]);
                        }
                        let avg = Math.pow(ratio.reduce((result, currentRatio) => {
                            return result *= currentRatio}), 1/ratio.length);
                        if (Math.abs(avg - 1) > this.minimumThreshold) {
                            data.push({ name: key, value: avg - 1, points: ratio.map(elem => (elem - 1))});
                        }
                    }
                }
                data.sort((a, b) => {
                    return (a.value - b.value);
                });
                data.map(elem => avgTime.push(parseFloat(elem.value)).toFixed(4));

                data.map(elem => {
                    let n = elem.points.length;
                    let mean = Number(parseFloat((elem.points.reduce((previousValue, currentValue) => {
                        return previousValue += currentValue}) / n).toFixed(4)));
                    let variance = elem.points.reduce((previousValue, currentValue) => {
                        return previousValue += Math.pow(currentValue - mean, 2);
                    }) / n;
                    let confidenceInterval = this.criticalValues[this.picked] * (variance / Math.sqrt(n));
                    errorIntervals.push([Number(parseFloat(mean - confidenceInterval).toFixed(4)),
                        Number(parseFloat(mean + confidenceInterval).toFixed(4))]);
                    // points.push([Math.min(...elem.points), Math.max(...elem.points)]);
                });
                this.testNames = [];
                data.map(elem => this.testNames.push(elem.name));


                return [
                    {
                        name: "Time difference",
                        type: 'column',
                        data: avgTime,
                        color: "#98c807",
                        tooltip: {
                            headerFormat: 'Test name: <b>{point.x}</b><br/>',
                            pointFormat: 'Time has changed by: <b>{point.y} s</b><br/>'
                        },
                    },
                    {
                        name: "Time ratio",
                        type: 'errorbar',
                        data: errorIntervals,
                        color: "#000000",
                        tooltip: {
                            pointFormat: 'Error range: <b>{point.low}-{point.high} s</b><br/>'
                        }
                    },
                ];
            },
            timeColumnChartOptions() {
                return {
                    //  credits - to hide licence logo
                    credits: {
                        enabled: false
                    },
                    title: {
                        text: "",
                    },
                    chart: {
                        height: '45%',
                        width: 1135
                    },
                    exporting: {
                        enabled: false
                    },
                    tooltip: {
                        shared: true
                    },
                    xAxis: {
                        categories: this.testNamesForChart
                    },
                    yAxis: {
                        labels: {
                            formatter: function () {
                                return this.axis.defaultLabelFormatter.call(this);
                            }
                        },
                        title: {
                            text: 'Time, sec',
                            style: {
                                color: "gray"
                            }
                        }
                    },
                    plotOptions: {
                        column: {
                            stacking: 'normal',
                            pointPadding: 0.1,
                            groupPadding: 0,
                            dataLabels: {
                                enabled: true,
                                format: '{point.value}',
                                style: {
                                    fontSize: "10px",
                                    fontWeight: 'bold',
                                    color: '#000000',
                                    textOutline: 0
                                },
                            }
                        }
                    },
                    series: this.series
                }
            },
        },
        methods: {
            changeThreshold(flag) {
                if (flag) {
                    this.minimumThreshold = parseFloat(Number(this.minimumThreshold) + 0.01).toFixed(2);
                } else {
                    this.minimumThreshold = parseFloat(Number(this.minimumThreshold) - 0.01).toFixed(2);
                }
                this.series;
                this.testNamesForChart;
            }
        },
        created() {
            this.series;
            this.testNamesForChart;
        }
    }
</script>

<style scoped>
    .column-chart {
        display: flex;
        flex-direction: column;
        background-color: #FFFFFF;
        margin: 20px 40px 0px 0;
        padding: 20px 12px 5px 10px;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
    .column-chart__title {
        font-size: 17px;
        text-align: center;
        margin: 0;
    }
    .params {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        margin: 5px 0 30px 20px;
    }
    .params__input-box {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .params_box {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin: 0 0 0 20px;
    }
    input[type="number"] {
        outline: none;
        -moz-appearance: textfield;
        margin: 0;
        padding: 5px;
        font-size: 14px;
        text-align: center;
        border-top: #BABABA solid 1px;
        border-bottom: #BABABA solid 1px;
        border-right: none;
        border-left: none;
    }
    input[type=number]::-webkit-inner-spin-button {
        -webkit-appearance: none;
    }
    .params__input-box__button {
        height: 29px;
        width: 29px;
        font-size: 20px;
        padding: 0 0 5px 0;
        text-align: center;
        outline: none;
    }
    .button-left {
        border: #BABABA solid 1px;
        border-top-left-radius: 2px ;
        border-bottom-left-radius: 2px;
    }
    .button-right {
        border: #BABABA solid 1px;
        border-top-right-radius: 2px;
        border-bottom-right-radius: 2px;
    }
    .params__radio {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        /*justify-content: center;*/
    }
    .params__radio_column {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    .params__radio label {
        font-size: 16px;
        color: #000000;
        margin-right: 15px;
    }
    input[type='radio'] {
        -webkit-appearance: none;
        cursor: pointer;
        width:18px;
        height:18px;
        margin: 0 5px 0 0;
        border-radius: 50%;
        outline: none;
        border: 2px solid #a0a0a0;
    }
    input[type='radio']:before {
        content: '';
        display: block;
        width: 60%;
        height: 60%;
        margin: 20% auto;
        border-radius: 50%;
    }
    input[type="radio"]:checked:before {
        background: #98c807;
    }
    input[type="radio"]:checked {
        border-color: #98c807;
    }
</style>
