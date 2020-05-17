<template>
    <div class="unstableTestsChart">
        <p class="unstableTestsChart__title">UNSTABLE TESTS' TIME</p>
        <div class="params">
            <p class="params__title">
                Percentile:
            </p>
            <div class="params__radio">
                <div class="params__radio_column" v-for="value in radioValues">
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
                radioValues: [5, 50, 95, 99]
            }
        },
        computed: {
            testNamesForChart() {
                return this.testNames;
            },
            confidenceInterval() {
                return (1/Math.sqrt(3)) * (this.picked / 100);
            },
            series() {
                let testsTime = [];
                let errorIntervals = [];
                this.testNames = [];
                this.unstableQueries.map(elem => {
                    testsTime.push(elem.newTime);
                    this.testNames.push(elem.testName);
                    errorIntervals.push(
                        [Number(parseFloat(elem.newTime - this.confidenceInterval).toFixed(4)),
                            Number(parseFloat(elem.newTime + this.confidenceInterval).toFixed(4))]);
                });
                return [
                    {
                        name: "Time of unstable test",
                        type: 'spline',
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
                        type: 'column',
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
