<template>
    <div class="splineChart">
        <highcharts :options="timeSplineOptions"></highcharts>
    </div>
</template>

<script>
    export default {
        name: "allTestsTimeSpline",
        props: {
            timePerformance: {
                type: Object,
                default: {}
            },
            allTestsHistory: {
                type: Array,
                default: []
            }
        },
        data() {
            return {
                testNames: [],
                minimumThreshold: 0.001,
                historyTime: {}
            }
        },
        computed: {
            testNamesForChart() {
                return this.testNames;
            },
            series() {
                let allCommitsData = {
                    current: {},
                    history: {}
                };
                // {y: Math.max(elem.allTests, 100), value: elem.allTests})
                for (let key in this.timePerformance) {
                    for (let i = 0; i !== this.allTestsHistory.length; ++i) {
                        if (this.allTestsHistory[i].timePerformance.hasOwnProperty(key)) {
                            let commitAvgTime = this.allTestsHistory[i].timePerformance[key].newTime.reduce(
                                (previousValue, currentValue) => {
                                    return previousValue += currentValue;
                                }) / this.allTestsHistory[i].timePerformance[key].newTime.length;
                            if (!(key in allCommitsData.history)) {
                                allCommitsData.history[key] = [commitAvgTime];
                                // console.log(allCommitsData.history);
                            } else {
                                allCommitsData.history[key].push(commitAvgTime);
                            }
                            allCommitsData.current[key] = this.timePerformance[key].newTime;
                        }
                    }
                }
                for (let key in allCommitsData.current) {
                    // avg in one current commit different small tests in each test
                    allCommitsData.current[key] = allCommitsData.current[key].reduce(
                        (previousValue, currentValue) => {
                            return previousValue += currentValue;
                        }) / allCommitsData.current[key].length;
                    // avg in commits
                    allCommitsData.history[key] = allCommitsData.history[key].reduce(
                        (previousValue, currentValue) => {
                            return previousValue += currentValue;
                        }) / allCommitsData.history[key].length;
                }
                let currentCommitData = [];
                let historyCommitsData = [];
                for (let key in allCommitsData.current) {
                    currentCommitData.push(parseFloat(allCommitsData.current[key].toFixed(4)));
                    historyCommitsData.push(parseFloat(allCommitsData.history[key].toFixed(4)));
                    this.testNames.push(key);
                }
                return [
                    {
                        name: "average of all tests",
                        data: historyCommitsData,
                        color: "#f8cd46",
                        type: 'area',
                        fillOpacity: 0.5,
                        tooltip: {
                            headerFormat: 'Test name: <b>{point.x}</b><br/>',
                            pointFormat: 'Average time: <b>{point.y} s</b><br/>'
                        }
                    },
                    {
                        name: "current commit",
                        data: currentCommitData,
                        type: 'spline',
                        color: "#98c807",
                        marker: {
                            radius: 2,
                            lineWidth: 0.5,
                            symbol: "circle",
                            lineColor: "#98c807",
                        },
                        tooltip: {
                            pointFormat: 'Current time: <b>{point.y} s</b><br/>'
                        }
                    }
                ]
            },
            timeSplineOptions() {
                return {
                    //  credits - to hide licence logo
                    credits: {
                        enabled: false
                    },
                    title: {
                        text: "TEST TIME OF ALL TESTS",
                        style: {
                            fontSize: "16px",
                        }
                    },
                    chart: {
                        height: '75%',
                        width: 700
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
                    yAxis: [
                        {
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
                        {
                            labels: {
                                formatter: function () {
                                    return this.axis.defaultLabelFormatter.call(this);
                                }
                            },
                            title: {
                                text: '',
                            }
                        }
                    ],
                    series: this.series
                }
            }
        },
    };
</script>

<style scoped>
    .splineChart {
        background-color: #FFFFFF;
        margin: 20px 100px 0 0;
        padding: 15px 15px 5px 8px;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
</style>
