<template>
    <div class="column-chart">
        <highcharts :options="columnChartOptions"></highcharts>
    </div>
</template>

<script>

    export default {
        name: "HistoryTestsColumnChart",
        props: {
            allTestsHistory: {
                type: Array,
                default: []
            }
        },
        computed: {
            commitsDates() {
                let dates = [];
                this.allTestsHistory.map(elem => {
                    let date = new Date(elem.commit.date);
                    const dtf = new Intl.DateTimeFormat('en', { year: 'numeric', month: 'short', day: '2-digit' });
                    const [{ value: mo },,{ value: da },,{ value: ye }] = dtf.formatToParts(date);
                    dates.push(`${da}-${mo}-${ye}`);
                });
                return dates;
            },
            series() {
                let allPassedTestsForChart = [];
                let allFailedTestsForChart = [];
                let allSkippedTestsForChart = [];
                this.allTestsHistory.map(elem => {
                    (elem.allTests !== 0) ?
                        allPassedTestsForChart.push({y: Math.max(elem.allTests, 100), value: elem.allTests}) :
                        allPassedTestsForChart.push({y: 0, value: elem.allTests});
                    (elem.failTests !== 0) ?
                        allFailedTestsForChart.push({y: Math.max(elem.failTests, 100), value: elem.failTests}) :
                        allFailedTestsForChart.push({y: 0, value: elem.failTests});
                    (elem.skippedTests !== 0) ?
                        allSkippedTestsForChart.push({y: Math.max(elem.skippedTests, 100), value: elem.skippedTests}) :
                        allSkippedTestsForChart.push({y: 0, value: elem.skippedTests});
                });
                return [
                    {
                        name: "Passed tests",
                        data: allPassedTestsForChart,
                        color: "#98c807"
                    },
                    {
                        name: "Failed tests",
                        data: allFailedTestsForChart,
                        color: "#d13814"
                    },
                    {
                        name: "Skipped tests",
                        data: allSkippedTestsForChart,
                        color: "#edd812"
                    },
                ]
            },
            columnChartOptions() {
                return {
                    //  credits - to hide licence logo
                    credits: {
                        enabled: false
                    },
                    title: {
                        text: "HISTORY OF ALL COMMITS",
                        style: {
                            fontSize: "16px",
                        }
                    },
                    chart: {
                        type: 'column',
                        height: '75%',
                        width: 700
                    },
                    exporting: {
                        enabled: false
                    },
                    xAxis: {
                        categories: this.commitsDates
                    },
                    yAxis: {
                        min: 0,
                        labels: {
                            formatter: function() {
                                return this.axis.defaultLabelFormatter.call(this);
                            }
                        },
                        title: {
                            text: 'Number of tests',
                            style: {
                                color: "gray"
                            }
                        }
                    },
                    tooltip: {
                        headerFormat: 'Commit from <b>{point.x}</b><br/>',
                        pointFormat: '{series.name}: <b>{point.value} tests</b>'
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
    };
</script>

<style scoped>
    .column-chart {
        background-color: #FFFFFF;
        margin: 20px 0px 0 0;
        padding: 15px 15px 5px 8px;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
</style>
