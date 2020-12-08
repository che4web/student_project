<template>
  <div id="app">
        <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light bg-light  ">
                <a class="navbar-brand" href="#">che</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <router-link class="nav-link" to="/">Студенты<span class="sr-only">(current)</span></router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/course/">Предметы</router-link>
                        </li>
                    </ul>
                </div>
            </nav> 
        </div>
        <div class="container">
    <router-view/>
        </div>
  </div>
</template>

<style>
</style>
