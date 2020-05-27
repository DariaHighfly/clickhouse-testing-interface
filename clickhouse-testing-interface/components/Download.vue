<template>
    <div class="download__description">
        <a :href="gitHubLink">
            <div class="download__description-box">
                <p class="download__description-box__number">TEST OUTPUT</p>
                <p class="download__description-box__text">DOWNLOAD</p>
            </div>
        </a>
    </div>

</template>

<script>
    export default {
        name: "Download",
        props: {
            commitName: {
                type: String,
                default: ""
            }
        },
        data() {
            return {
                gitHubLinkHead: "https://clickhouse-test-reports.s3.yandex.net/0/",
                gitHubLinkTail: "/performance_comparison/output.7z",
                linkToDownload: "output.7z"
            }
        },
        computed: {
            gitHubLink() {
                return this.gitHubLinkHead + this.commitName + this.gitHubLinkTail;
            }
        }
    }
</script>

<style scoped>
    .download__description {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        margin-bottom: 40px;
    }
    .download__description a {
        text-decoration: none;
    }
    .download__description-box {
        cursor: pointer;
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
        transform: scale(1);
        transition: 0.15s all ease;
    }
    .download__description-box:hover {
        transform: scale(1.05);
        cursor: pointer;
    }
    .download__description-box:first-child {
        padding-right: 18px;
        padding-left: 18px;
    }
    .download__description-box__number {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 36px;
        color: black;
        margin: 0;
    }
    .download__description-box__text {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 14px;
        width: 90px;
        color: black;
        text-align: center;
        margin: 0;
    }
</style>

