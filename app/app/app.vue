<script setup lang="ts">
const toaster = {
  position: "bottom-right",
} as const
</script>

<template>
  <UApp :toaster="toaster">
    <NuxtPage />
  </UApp>
</template>
