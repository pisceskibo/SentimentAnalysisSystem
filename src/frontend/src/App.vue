<script setup>
import { ref } from "vue"
import axios from "axios"

const text = ref("")
const result = ref(null)
const loading = ref(false)

const analyzeSentiment = async () => {

  loading.value = true

  try {
    const response = await axios.post(
      "http://localhost:5000/predict",
      {
        text: text.value
      }
    )
    result.value = response.data

  } catch (error) {
    result.value = {
      status: "error",
      message:
        error.response?.data?.message ||
        "Không kết nối được API"
    }
  }

  loading.value = false
}
</script>

<template>

  <div class="container">

    <h1>Phân tích cảm xúc bình luận xe ô tô</h1>

    <textarea
      v-model="text"
      placeholder="Nhập bình luận..."
    />

    <br>

    <button @click="analyzeSentiment"> Phân tích </button>

    <div
      v-if="loading"
      class="result"
    >
      Đang xử lý...
    </div>

    <div
      v-if="result"
      class="result"
    >

      <p>
        <b>Sentiment:</b>
        {{ result.sentiment }}
      </p>

      <p>
        <b>Confidence:</b>
        {{ result.confidence_score }}
      </p>

    </div>

  </div>

</template>

<style>

.container{
  width:700px;
  margin:auto;
  margin-top:50px;
}

textarea{
  width:100%;
  height:150px;
}

.result{
  margin-top:20px;
}

h1{
  text-align:center;
  font-size: 42px;
  line-height: 1.2;
  margin-bottom: 20px;
}

</style>