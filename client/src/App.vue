<template>
  <main>
    <p class="error" v-if="error">{{ error }}</p>
    <p v-if="isLoading">Loading...</p>
    <ul v-else>
      <li :key="todo.id" v-for="todo in todos">
        <button @click.prevent="deleteTodo(todo.id)">X</button>
        {{ todo.title }} - {{ todo.description }}
      </li>
    </ul>
    <form>
      <div>
        <input v-model="form.title" type="text" placeholder="Todo Title" />
      </div>
      <div>
        <input
          v-model="form.description"
          type="text"
          placeholder="Description"
        />
      </div>
      <button @click.prevent="addTodo">Add Todo</button>
    </form>
  </main>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios"

const todos = ref([]);
const isLoading = ref(true);
const error = ref(null);

const form = ref({
  title: null,
  description: null,
});

async function fetchTodos() {
  try {
    const res = await axios.get("/api/todos");
    todos.value = res.data.todos;
  } catch (e) {
    error.value = e.response.data?.message ?? "Could not load todos";
  }

  isLoading.value = false;
}

async function addTodo() {
  try {
    const res = await axios.post("/api/todos", form.value);
    todos.value.push(res.data.todo);
  } catch (e) {
    console.log(e);
    error.value = e.response.data?.message ?? "Could not add todo";
  }
}

async function deleteTodo(id) {
  try {
    await axios.delete(`/api/todos/${id}`)
    todos.value = todos.value.filter(todo => todo.id != id)
  } catch (e) {
    error.value = e.response.data?.message ?? "Could not remove todo";
  }
}

fetchTodos();
</script>
