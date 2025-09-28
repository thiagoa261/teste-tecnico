import { useAuthStore } from "~/stores/auth";

export default defineNuxtRouteMiddleware(async (to) => {
	const auth = useAuthStore();
	const router = useRouter();

	if (auth.isLoggedIn) {
		const user = await auth.fetchMe();
		if (!user) return router.push("/login");
	}

	if (!auth.isLoggedIn && to.path !== "/login") return router.push("/login");

	if (auth.isLoggedIn && to.path === "/login") return router.push("/");
});
