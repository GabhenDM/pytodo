import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'

import {BootstrapVue,IconsPlugin} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Vuex)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
