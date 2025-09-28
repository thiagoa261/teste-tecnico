import { defineStore } from "pinia";
import axios from "axios";
import type { ILoginResponse, IMeResponse } from "~/types/auth";

export const useAuthStore = defineStore("auth", {
	state: () => ({
		token: null as string | null,
		user: null as string | null,
	}),

	getters: {
		isLoggedIn: (state) => !!state.token,
	},

	actions: {
		async login(username: string, password: string) {
			const config = useRuntimeConfig();
			try {
				const response = await axios.post<ILoginResponse>(`${config.public.apiUrl}/auth/login`, { username, password });

				if (!response.data.session_token) throw new Error("token da sessão não encontrado!");

				this.token = response.data.session_token;
				return true;
			} catch {
				this.token = null;
				return false;
			}
		},

		async fetchMe() {
			if (!this.token) return null;
			const config = useRuntimeConfig();
			try {
				const response = await axios.get<IMeResponse>(`${config.public.apiUrl}/auth/me`, { headers: { token: this.token } });

				if (!response.data.username) throw new Error("Usuário não encontrado!");

				this.user = response.data.username;
				return this.user;
			} catch {
				this.logout();
				return null;
			}
		},

		async logout() {
			const config = useRuntimeConfig();
			try {
				await axios.post(`${config.public.apiUrl}/auth/logout`, {}, { headers: { token: this.token } });
			} catch {
			} finally {
				this.token = null;
				this.user = null;
			}
		},
	},

	persist: true,
});
