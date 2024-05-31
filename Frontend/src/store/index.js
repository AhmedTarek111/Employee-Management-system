// src/store/index.js
import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: null
  },
  mutations: {
    auth_success(state, token) {
      state.token = token
    },
    auth_error(state) {
      state.token = ''
    },
    set_user(state, user) {
      state.user = user
    },
    logout(state) {
      state.token = ''
      state.user = null
    }
  },
  actions: {
    loginUser({ commit }, user) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://127.0.0.1:8000/api/token/', data: user, method: 'POST' })
          .then(resp => {
            const token = resp.data.access
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
            commit('auth_success', token)
            commit('set_user', resp.data.user)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    logout({ commit }) {
      return new Promise((resolve) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    }
  },
  getters: {
    isAuthenticated: state => !!state.token,
    authStatus: state => state.status,
  }
})
