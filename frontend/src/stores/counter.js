import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios";

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    axios.post('/api/count').then(res => {
      count.value = res.data.count
    })
  }

  return { count, doubleCount, increment }
})
