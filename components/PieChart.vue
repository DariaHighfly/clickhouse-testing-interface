<template>
    <div class="pie-chart">
        <highcharts :options="pieChartOptions"></highcharts>
    </div>

</template>

<script>
    export default {
        name: "PieChart",
        props: {
            commitName: {
                type: String,
                default: ""
            },
            allTests: {
                type: Number,
                default: 0
            },
            failTests: {
                type: Number,
                default: 0
            },
            skippedTests: {
                type: Number,
                default: 0
            },

        },
        computed: {
            sum() {
                return this.allTests + this.failTests + this.skippedTests;
            },
            series() {
                let columnHeightFailed = (this.failTests !== 0) ? Math.max(this.failTests, 15) : 0;
                let columnHeightSkipped = (this.skippedTests !== 0) ? Math.max(this.skippedTests, 15) : 0;
                let columnHeightPassed = (this.allTests !== 0) ? Math.max(this.allTests, 15) : 0;
                return [{
                    name: 'Results',
                    colorByPoint: true,
                    value: this.failTests,
                    innerSize: '70%',
                    zMin: 0,
                    data: [
                        {
                            name: 'Failed tests',
                            color: "#d13814",
                            y: columnHeightFailed,
                            value: this.failTests
                        },
                        {
                            name: 'Skipped tests',
                            color: "#edd812",
                            y: columnHeightSkipped,
                            value: this.skippedTests
                        },
                        {
                            name: 'Passed tests',
                            color: "#98c807",
                            y: columnHeightPassed,
                            value: this.allTests
                        }
                    ]
                }];
            },
            pieChartOptions() {
                return {
                    //  credits - to hide licence logo
                    credits: {
                        enabled: false
                    },
                    title: {
                        text: " TOTAL TESTS:<br>" + this.sum,
                        style: {
                            fontSize: "17px",
                        },
                        align: 'center',
                        verticalAlign: 'middle',
                        y: 2
                    },
                    chart: {
                        type: 'pie',
                        height: '70%',
                        width: 395
                    },
                    exporting: {
                        enabled: false
                    },
                    xAxis: {
                        type: 'category'
                    },
                    yAxis: {
                        labels: {
                            formatter: function() {
                                return this.axis.defaultLabelFormatter.call(this);
                            }
                        }
                    },
                    tooltip: {
                        pointFormat: '{series.name}: <b>{point.value} tests</b>'
                    },
                    plotOptions: {
                        pie: {
                            allowPointSelect: true,
                            cursor: 'pointer',
                            dataLabels: {
                                enabled: false
                            },
                            showInLegend: true,
                        },
                    },
                    series: this.series
                }
            },
        }
    }
</script>

<style scoped>
    .pie-chart {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        background-color: #FFFFFF;
        margin: 20px 20px 0 0;
        padding: 10px 20px 5px 0;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
    .pie-chart__description {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-top: 11px;
    }
    .pie-chart__description-box {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: flex-start;
        background-color: #f8cd46;
        padding: 10px 12px 10px 12px;
        margin-bottom: 10px;
        border-radius: 2px;
        transform: scale(1);
        transition: 0.15s all ease;
    }
    .pie-chart__description-box:hover {
        transform: scale(1.1);
        cursor: pointer;
    }
    .pie-chart__description-box__number {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 34px;
        color: black;
        margin: 0;
    }
    .pie-chart__description-box__text {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 13px;
        color: black;
        text-align: left;
        padding-left: 10px;
        padding-top: 5px;
        margin: 0;
    }
</style>
