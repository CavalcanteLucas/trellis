<script>
import axios from "axios";

export default {
  data() {
    return {
      inputNumber: "",
      responseMessage: "",
      responseStatus: "",
      responseIsLoading: false,
    };
  },
  computed: {
    showErrorMessage() {
      return this.responseStatus.includes("error");
    },
    showResponseMessage() {
      return this.responseStatus.includes("ok");
    },
  },
  methods: {
    validateNumber() {
      this.inputNumber = this.inputNumber.replace(/\D/g, "");
    },
    clearText() {
      this.inputNumber = "";
      this.responseMessage = "";
      this.responseStatus = "";
    },
    async getNumToEnglish() {
      try {
        let response = await axios.get("http://localhost:8000/num_to_english", {
          params: { number: this.inputNumber },
        });
        this.responseStatus = response.data.status;
        this.responseMessage = response.data.num_in_english;
      } catch (error) {
        this.responseStatus = error.response.data.status || "error";
        this.responseMessage =
          error.response.data.message || "Error fetching data";
      }
    },
    async postNumToEnglish() {
      this.responseIsLoading = true;
      this.responseStatus = "";
      this.responseMessage = "";
      setTimeout(async () => {
        try {
          let response = await axios.post(
            "http://localhost:8000/num_to_english",
            { number: String(this.inputNumber) },
          );
          this.responseStatus = response.data.status;
          this.responseMessage = response.data.num_in_english;
        } catch (error) {
          this.responseStatus = error.response.data.status || "error";
          this.responseMessage =
            error.response.data.message || "Error fetching data";
        }
        this.responseIsLoading = false;
      }, 500);
    },
  },
};
</script>

<template>
  <div class="w-xs">
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="">
        <label
          for="inputNumber"
          class="block text-gray-700 text-sm font-bold text-left mt-1 mb-1"
        >
          Translate number into English words:
        </label>
        <div class="relative w-full">
          <input
            v-model="inputNumber"
            id="inputNumber"
            type="text"
            placeholder="Input number"
            min="0"
            :maxlength="15"
            class="border-2 border-gray-200 rounded w-full py-2 px-3 pr-10 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-sm"
            @input="validateNumber"
            @keydown.enter.prevent
          />
          <button
            v-if="inputNumber"
            @click="clearText"
            class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
          >
            ✖
          </button>
        </div>
        <div class="h-6 p-1">
          <p v-if="showErrorMessage" class="text-red-600 text-xs italic">
            {{ responseMessage }}
          </p>
        </div>
        <div class="mb-6">
          <div
            class="w-full p-2 border border-gray-200 rounded-md text-gray-700 text-sm border-2 bg-gray-100 h-38 text-left"
          >
            <p
              v-if="showResponseMessage && !responseIsLoading"
              class="response-message-text"
            >
              {{ responseMessage }}.
            </p>
            <div v-if="responseIsLoading" class="spinner w-18 mr-6"></div>
          </div>
        </div>
      </div>
      <div class="flex items-center justify-between px-6">
        <button
          @click="getNumToEnglish"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-18"
          type="button"
        >
          GET
        </button>
        <button
          @click="postNumToEnglish"
          class="bg-blue-500 hover:bg-blue-700 white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-18"
          type="button"
        >
          POST
        </button>
      </div>
    </form>
    <p class="text-center text-gray-500 text-xs">
      by
      <a href="mailto:lucascpcavalcante@gmail.com">Lucas Cavalcante</a>
      @ 2025
    </p>
  </div>
</template>

<style scoped></style>
