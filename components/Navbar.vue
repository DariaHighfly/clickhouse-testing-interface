<template>
    <div class="navbar__block">
        <div>
            <p class="navbar__title">Performance</p>
            <p class="navbar__title">comparison of analytical DBMS</p>
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
        background-color: #FFFFFF;
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
