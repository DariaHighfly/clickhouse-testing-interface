<template>
    <div class="columnChart">
        <p class="columnChart__title">TIME PERFORMANCE OF CURRENT COMMIT</p>
        <div class="params">
            <p class="params__title">
                Minimum Threshold (abs):
            </p>
            <div class="params__input-box">
                <button class="params__input-box__button button-left" v-on:click="changeThreshold(0)">-</button>
                <input class="params__input-box__input" type="number" v-model="minimumThreshold" :min="0" :max="10000" step="0.001">
                <button class="params__input-box__button button-right" v-on:click="changeThreshold(1)">+</button>
            </div>
        </div>
        <highcharts :options="timeColumnChartOptions"></highcharts>
    </div>
</template>

<script>
    export default {
        name: "TimePerformanceColumnChart",
        props: {
            timePerformance: {
                type: Object,
                default: {}
            }
        },
        data() {
            return {
                testNames: [],
                minimumThreshold: 0.001,
            }
        },
        computed: {
            testNamesForChart() {
                return this.testNames;
            },
            series() {
                let data = [];
                let avgTime = [];
                for (let key in this.timePerformance) {
                    // Average of time difference
                    let currentAvgTime = this.timePerformance[key].reduce(
                        (previousValue, currentValue) => {
                            return previousValue += currentValue;
                        }) / this.timePerformance[key].length;
                    if (Math.abs(currentAvgTime) > this.minimumThreshold) {
                        avgTime.push({name: key, avgTime: currentAvgTime});
                    }
                }
                avgTime.sort((a, b) => {
                    return (a.avgTime - b.avgTime);
                });
                avgTime.map(elem => data.push(elem.avgTime));
                this.testNames = [];
                avgTime.map(elem => this.testNames.push(elem.name));
                return [
                    {
                        name: "Time difference",
                        data: data,
                        color: "#98c807"
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
                        type: 'column',
                        height: '75%',
                    },
                    exporting: {
                        enabled: false
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
                    },
                    tooltip: {
                        headerFormat: 'Test name: <b>{point.x}</b><br/>',
                        pointFormat: 'Time has changed by: <b>{point.y} s</b>'
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
            }
        },
        methods: {
            changeThreshold(flag) {
                flag ? (this.minimumThreshold += 0.001) : (this.minimumThreshold -= 0.001);
                this.series;
            }
        },
        created() {
            this.series;
            this.testNamesForChart;
        }
    }
</script>

<style scoped>
    .columnChart {
        display: flex;
        flex-direction: column;
        min-width: 600px;
    }
    .columnChart__title {
        font-size: 16px;
        text-align: center;
        margin: 0;
    }
    .params {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin: 30px 0 30px 20px;
    }
    .params__input-box {
        display: flex;
        flex-direction: row;
        align-items: center;
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
</style>
