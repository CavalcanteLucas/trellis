import { createRouter, createWebHistory } from "vue-router";
import Landing from "./pages/Landing.vue";

const routes = [
  {
    path: "/test",
    name: "landing",
    component: Landing,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
