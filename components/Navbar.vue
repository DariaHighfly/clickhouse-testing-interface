<template>
    <div class="navbar__block">
        <div class="navbar">
            <div>
                <p class="navbar__title">Performance</p>
                <p class="navbar__title">comparison of analytical DBMS</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>
    .navbar__block {
        width: 100%;
        color: black;
        margin: 10px 0 15px 0px;
        background-color: #FFFFFF;
    }
    .navbar {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .navbar__title {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 25px;
        display: flex;
        justify-content: flex-start;
        padding: 0;
        margin: 0;
    }
</style>
