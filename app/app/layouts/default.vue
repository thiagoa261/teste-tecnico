<script setup lang="ts"></script>

<template>
	<div>
		<Header />

		<UMain class="my-5">
			<div class="container mx-auto px-3">
				<slot />
			</div>
		</UMain>

		<Footer />
	</div>
</template>
