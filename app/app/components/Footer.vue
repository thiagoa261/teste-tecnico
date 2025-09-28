<script setup lang="ts"></script>

<template>
	<UFooter>
		<template #left>
			<p class="text-muted text-sm">Desenvolvido por Thiago Aio</p>
		</template>

		<template #right>
			<UButton
				icon="i-simple-icons-linkedin"
				color="neutral"
				variant="ghost"
				to="https://www.linkedin.com/in/thiagoaio"
				target="_blank"
				aria-label="LinkedIn"
			/>

			<UButton
				icon="i-simple-icons-github"
				color="neutral"
				variant="ghost"
				to="https://github.com/thiagoa261"
				target="_blank"
				aria-label="GitHub"
			/>
		</template>
	</UFooter>
</template>
