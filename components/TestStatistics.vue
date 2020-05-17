<template>
    <div class="pie-chart__description">
        <div class="pie-chart__description-box">
            <p class="pie-chart__description-box__number">{{this.allTests}}</p>
            <p class="pie-chart__description-box__text">TESTS<br/>PASSED</p>
        </div>
        <div class="pie-chart__description-box">
            <p class="pie-chart__description-box__number">{{this.failTests}}</p>
            <p class="pie-chart__description-box__text">TESTS<br/>FAILED</p>
        </div>
        <div class="pie-chart__description-box">
            <p class="pie-chart__description-box__number">{{this.skippedTests}}</p>
            <p class="pie-chart__description-box__text">TESTS<br/>SKIPPED</p>
        </div>
    </div>

</template>

<script>
    export default {
        name: "TestStatistics",
        props: {
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
            }
        }
    }
</script>

<style scoped>
    .pie-chart__description {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    .pie-chart__description-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #FFFFFF;
        margin: 20px 20px 0 0;
        padding: 21px 17px 26px 17px;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
    .pie-chart__description-box:first-child {
        padding-right: 18px;
        padding-left: 18px;
    }
    .pie-chart__description-box__number {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 36px;
        color: black;
        margin: 0;
    }
    .pie-chart__description-box__text {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 14px;
        width: 90px;
        color: black;
        text-align: center;
        margin: 0;
    }
</style>

