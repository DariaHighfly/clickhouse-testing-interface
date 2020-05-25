<template>
    <div class="unstableTestsChart">
        <p class="unstableTestsChart__title">UNSTABLE TESTS' TIME</p>
        <div class="params">
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
        <highcharts :options="unstableTestsChartOptions"></highcharts>
    </div>
</template>

<script>

    export default {
        name: "UnstableTestsChart",
        props: {
            unstableQueries: {
                type: Array,
                default: []
            }
        },
        data() {
            return {
                testNames: [],
                picked: 5,
                criticalValues: {
                    5: 0.65,
                    50: 0.68,
                    95: 1.96,
                    99: 2.58
                },
                currentUnstableQueries: [...this.unstableQueries]
            }
        },
        computed: {
            testNamesForChart() {
                return this.testNames;
            },
            series() {
                let testsTime = [];
                let errorIntervals = [];
                this.testNames = [];
                this.currentUnstableQueries.sort((a,b) => {
                    return (a.newTime - b.newTime);
                });
                this.currentUnstableQueries.map(elem => {
                    this.testNames.push(elem.testName);
                    let n = elem.rightRunTimes.length;
                    if (n === 0) {
                        testsTime.push(elem.newTime);
                        errorIntervals.push([]);
                    } else {
                        let variance = elem.rightRunTimes.reduce((previousValue, currentValue) => {
                            return previousValue += Math.pow(currentValue - elem.newTime, 2);
                        }) / n;
                        let confidenceInterval = this.criticalValues[this.picked] * (variance / Math.sqrt(n));
                        let mean = Number(parseFloat((elem.rightRunTimes.reduce((previousValue, currentValue) => {
                            return previousValue += currentValue}) / n).toFixed(4)));
                        testsTime.push(mean);
                        errorIntervals.push([
                            Number(parseFloat(mean - confidenceInterval).toFixed(4)),
                            Number(parseFloat(mean + confidenceInterval).toFixed(4))]
                        );
                    }
                });
                return [
                    {
                        name: "Time of unstable test",
                        type: 'column',
                        data: testsTime,
                        color: "#98c807",
                        tooltip: {
                            headerFormat: 'Test name: <b>{point.x}</b><br/>',
                            pointFormat: '{series.name}: <b>{point.y} s</b><br/>'
                        }
                    },
                    {
                        name: "Time error",
                        type: 'errorbar',
                        data: errorIntervals,
                        color: "#d13814",
                        tooltip: {
                            pointFormat: 'Error range: <b>{point.low}-{point.high} s</b><br/>'
                        }
                    }
                ]
            },
            // BOX PLOT
            // // BOX PLOT params: the smallest observation (sample minimum), lower quartile (Q1),
            // // median (Q2), upper quartile (Q3), and largest observation (sample maximum)
            // series() {
            //     let testsTime = [];
            //     this.testNames = [];
            //     this.currentUnstableQueries.map(elem => {
            //         this.testNames.push(elem.testName);
            //         let n = elem.rightRunTimes.length;
            //         if (n === 0) {
            //             testsTime.push([elem.newTime, elem.newTime, elem.newTime, elem.newTime, elem.newTime]);
            //         } else {
            //             let variance = elem.rightRunTimes.reduce((previousValue, currentValue) => {
            //                 return previousValue += Math.pow(currentValue - elem.newTime, 2);
            //             }) / n;
            //             let confidenceInterval = this.criticalValues[this.picked] * (variance / Math.sqrt(n));
            //             let mean = Number(parseFloat((elem.rightRunTimes.reduce((previousValue, currentValue) => {
            //                 return previousValue += currentValue}) / n).toFixed(4)));
            //             let min = Number(parseFloat(Math.min(...elem.rightRunTimes)).toFixed(4));
            //             let max = Number(parseFloat(Math.max(...elem.rightRunTimes)).toFixed(4));
            //             testsTime.push([min, Number(parseFloat(mean - confidenceInterval).toFixed(4)),
            //                 mean, Number(parseFloat(mean + confidenceInterval).toFixed(4)), max]);
            //         }
            //     });
            //     return [{
            //         name: 'Observations',
            //         data: testsTime,
            //         type: 'boxplot'
            //     }];
            // },
            unstableTestsChartOptions() {
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
                    tooltip: {
                        shared: true
                    },
                    exporting: {
                        enabled: false
                    },
                    xAxis: [{
                        categories: this.testNamesForChart
                    }],
                    yAxis: {
                        labels: {
                            formatter: function() {
                                return this.axis.defaultLabelFormatter.call(this);
                            }
                        },
                        title: {
                            text: 'Time, s',
                            style: {
                                color: "gray"
                            }
                        }
                    },
                    series: this.series
                }
            }
        },
        created() {
            this.series;
            this.confidenceInterval;
            this.testNamesForChart;
        }
    };
</script>

<style scoped>
    .unstableTestsChart {
        display: flex;
        flex-direction: column;
        justify-content: center;
        background-color: #FFFFFF;
        margin: 20px 40px 0 0;
        padding: 20px 12px 5px 10px;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
    .unstableTestsChart__title {
        font-size: 16px;
        margin: 0;
    }
    .params {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin: 20px 0 30px 20px;
    }
    .params__title {
        margin: 0 0 20px 0;
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
