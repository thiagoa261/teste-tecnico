<script setup lang="ts">
import * as z from "zod";
import type { FormSubmitEvent } from "@nuxt/ui";
import { useAuthStore } from "~/stores/auth";

const router = useRouter();
const auth = useAuthStore();
const loading = ref(false);
const { toastError, toastSuccess } = useAppToast();

const fields = [
	{
		name: "usuario",
		type: "text" as const,
		label: "Usuário",
		placeholder: "Digite seu usuário",
		required: true,
	},
	{
		name: "senha",
		label: "Senha",
		type: "password" as const,
		placeholder: "Digite sua senha",
		required: true,
	},
];

const schema = z.object({
	usuario: z.string("Usuário é obrigatório"),
	senha: z.string("Senha é obrigatória"),
});

type Schema = z.output<typeof schema>;

async function onSubmit(payload: FormSubmitEvent<Schema>) {
	try {
		loading.value = true;

		const response = await auth.login(payload.data.usuario, payload.data.senha);

		if (!response) throw new Error("Erro ao realizar login. Tente novamente.");

		toastSuccess("Login realizado com sucesso!");
		router.push("/");
	} catch (error) {
		toastError("Erro ao realizar login.");
	} finally {
		loading.value = false;
	}
}

definePageMeta({
	layout: "empty",
});
</script>

<template>
	<div class="flex items-center justify-center min-h-screen">
		<UPageCard class="w-full max-w-md">
			<UAuthForm
				:schema="schema"
				title="Acesso"
				description="Digite suas credenciais para acessar sua conta."
				icon="i-lucide-user"
				:fields="fields"
				:submit="{ label: 'Entrar', loading }"
				@submit="onSubmit"
			/>
		</UPageCard>
	</div>
</template>
