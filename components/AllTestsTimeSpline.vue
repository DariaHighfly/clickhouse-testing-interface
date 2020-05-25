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
                            } else {
                                allCommitsData.history[key].push(commitAvgTime);
                            }
                        }
                    }
                    let testAvgTime = this.timePerformance[key].reduce(
                        (allQueriesAvg, currentValue) => {
                            let commitAvgTime = currentValue.newTime.reduce(
                                (oneQueryAvg, nowValue) => {
                                    return oneQueryAvg += nowValue;
                                }) / currentValue.newTime.length;
                            return allQueriesAvg += commitAvgTime;
                        }, 0) / this.timePerformance[key].length;
                    allCommitsData.current[key] = testAvgTime;
                }
                for (let key in allCommitsData.history) {
                    // avg in commits
                    allCommitsData.history[key] = allCommitsData.history[key].reduce(
                        (previousValue, currentValue) => {
                            return previousValue += currentValue;
                        }) / allCommitsData.history[key].length;
                }
                let currentData = [];
                for (let key in allCommitsData.current) {
                    currentData.push({name: key, currentTime: allCommitsData.current[key], historyTime: allCommitsData.history[key]});
                }
                currentData.sort((a,b) => {
                    return Math.abs(a.currentTime - a.historyTime) - Math.abs(b.currentTime - b.historyTime);
                });
                let currentCommitData = [];
                let historyCommitsData = [];
                currentData.map((elem, index) => {
                    currentCommitData.push(parseFloat(elem.currentTime.toFixed(4)));
                    historyCommitsData.push(parseFloat(elem.historyTime.toFixed(4)));
                    this.testNames.push(elem.name);
                });
                return [
                    {
                        name: "average of all tests",
                        type: 'column',
                        data: historyCommitsData,
                        color: "#f8cd46",
                        pointPadding: 0.1,
                        groupPadding: 0,
                        tooltip: {
                            headerFormat: 'Test name: <b>{point.x}</b><br/>',
                            pointFormat: 'Average time: <b>{point.y} s</b><br/>'
                        }
                    },
                    {
                        name: "current commit",
                        type: 'scatter',
                        data: currentCommitData,
                        color: "#98c807",
                        marker: {
                            radius: 2.5,
                            lineWidth: 0.5,
                            symbol: "circle",
                            lineColor: "#98c807",
                        },
                        tooltip: {
                            headerFormat: 'Test name: <b>{point.x}</b><br/>',
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
                        text: "AVERAGE TEST TIME OF ALL TESTS",
                        style: {
                            fontSize: "16px",
                        }
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
