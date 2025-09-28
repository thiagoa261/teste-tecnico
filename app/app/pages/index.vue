<script setup lang="ts">
import { eTipoInput } from "~/types/enums";
import type { IIAResponse } from "~/types/response";
import axios from "axios";

const config = useRuntimeConfig();
const authStore = useAuthStore();
const { toastError, toastSuccess } = useAppToast();

const loading = ref(false);
const tiposInput = ref([eTipoInput.TEXTO, eTipoInput.ARQUIVO]);
const selectedTipo = ref(eTipoInput.TEXTO);
const file = ref<File | null>(null);
const emailBody = ref("");
const iaResponse = ref<IIAResponse>({
	categoria: "",
	justificativa: "",
	resposta_sugerida: "",
});

async function submitForm() {
	loading.value = true;

	if (selectedTipo.value === eTipoInput.TEXTO) {
		try {
			if (!emailBody.value) {
				toastError("O corpo do email não pode ser vazio.");
				return;
			}

			const token = await authStore.getToken();
			if (!token) {
				toastError("Usuário não autenticado.");
				return;
			}

			const response = await axios.post(
				`${config.public.apiUrl}/email/processar`,
				{ content: emailBody.value },
				{ headers: { token } },
			);

			if (response.status !== 200) {
				toastError("Erro ao processar email.");
				return;
			}

			iaResponse.value = response.data;
			toastSuccess("Email processado com sucesso.");
		} catch (err) {
			toastError("Erro ao processar email.");
		} finally {
			loading.value = false;
		}
	}

	if (selectedTipo.value === eTipoInput.ARQUIVO) {
		try {
			if (!file.value) {
				toastError("Selecione um arquivo.");
				return;
			}

			const token = await authStore.getToken();
			if (!token) {
				toastError("Usuário não autenticado.");
				return;
			}

			const formData = new FormData();
			formData.append("file", file.value);

			const response = await axios.post(`${config.public.apiUrl}/email/processar/file`, formData, {
				headers: {
					"Content-Type": "multipart/form-data",
					token,
				},
			});

			if (response.status !== 200) {
				toastError("Erro ao processar email.");
				return;
			}

			iaResponse.value = response.data;
			toastSuccess("Arquivo processado com sucesso.");
		} catch (err) {
			toastError("Erro ao processar arquivo.");
		} finally {
			loading.value = false;
		}
	}
}

function clear() {
	emailBody.value = "";
	file.value = null;
	iaResponse.value = {
		categoria: "",
		justificativa: "",
		resposta_sugerida: "",
	};
	loading.value = false;
}

definePageMeta({
	layout: "default",
});
</script>

<template>
	<div class="flex w-full flex-col md:flex-row gap-5">
		<UCard class="w-full md:w-1/2">
			<template #header>
				<div class="flex items-center gap-3 justify-center">
					<Icon name="i-lucide-mail" class="w-7 h-7" />
					<span class="font-semibold">Email para Análise</span>
				</div>
			</template>

			<UFormField label="Selecionar Tipo de Entrada:" class="mb-6">
				<USelectMenu v-model="selectedTipo" :items="tiposInput" class="w-full" :disabled="loading" />
				<template #error><div></div></template>
			</UFormField>

			<UForm ref="form" class="space-y-2">
				<UFormField label="Corpo do Email:" name="body" v-if="selectedTipo === eTipoInput.TEXTO">
					<UTextarea v-model="emailBody" class="w-full" :rows="12" style="resize: none" :disabled="loading" />
					<template #error><div></div></template>
				</UFormField>

				<UFormField label="Upload do Email:" v-if="selectedTipo === eTipoInput.ARQUIVO">
					<UFileUpload
						v-model="file"
						label="Selecione um arquivo de email"
						class="min-h-48 w-full"
						accept=".pdf,.txt"
						:disabled="loading"
					/>
					<template #error><div></div></template>
				</UFormField>
			</UForm>

			<template #footer>
				<div class="flex justify-end">
					<UButton @click="submitForm" :loading="loading" icon="i-lucide-send">Enviar para Análise</UButton>
				</div>
			</template>
		</UCard>

		<UCard class="w-full md:w-1/2">
			<template #header>
				<div class="flex items-center gap-3 justify-center">
					<Icon name="i-lucide-cpu" class="w-7 h-7" />
					<span class="font-semibold">Resposta da IA</span>
				</div>
			</template>

			<div class="flex flex-col gap-3">
				<UFormField label="Classificação:">
					<UInput class="w-full" :disabled="true" v-model="iaResponse.categoria" />
				</UFormField>

				<UFormField label="Justificativa da classificação:">
					<UTextarea class="w-full" :rows="3" style="resize: none" :disabled="true" v-model="iaResponse.justificativa" />
				</UFormField>

				<UFormField label="Resposta Sugerida:">
					<UTextarea class="w-full" :rows="7" style="resize: none" :disabled="true" v-model="iaResponse.resposta_sugerida" />
				</UFormField>
			</div>

			<template #footer>
				<div class="flex justify-end">
					<UButton @click="clear" color="error" icon="i-lucide-trash" :disabled="loading">Limpar</UButton>
				</div>
			</template>
		</UCard>
	</div>
</template>
