<template>
    <div class="title">
        <p class="title__text">RESULTS OF THE COMMIT №
            <a :href="linkToGitHubCommit"><b>{{this.commitName}}</b></a></p>
    </div>
</template>

<script>
    export default {
        name: "Title",
        props: {
            commitName: {
                type: String,
                default: ""
            }
        },
        data() {
            return {
                linkBase: "https://github.com/ClickHouse/ClickHouse/commit/",
            }
        },
        computed: {
            linkToGitHubCommit() {
                return this.linkBase + this.commitName;
            }
        }
    }
</script>

<style scoped>
    .title {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #FFFFFF;
        margin: 20px 20px 0 0;
        width: 100%;
        max-width: 1158px;
        border-radius: 4px;
        -webkit-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        -moz-box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
        box-shadow: 6px 7px 13px 2px rgba(0,0,0,0.11);
    }
    .title__text {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 16px;
        margin: 1em 0 1em 0;
    }
    .title__text a {
        text-decoration: none;
        cursor: pointer;
        color: #000000;
    }
    .title__text a :visited {
        color: #000000;
    }
</style>
