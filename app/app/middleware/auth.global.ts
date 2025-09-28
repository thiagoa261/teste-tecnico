import { useAuthStore } from "~/stores/auth";

export default defineNuxtRouteMiddleware(async (to) => {
	const auth = useAuthStore();
	const router = useRouter();

	if (!auth.isLoggedIn && to.path !== "/login") {
		return router.push("/login");
	}

	const lastCheck = useState<number>("lastCheck", () => 0);
	const now = Date.now();

	if (auth.isLoggedIn && now - lastCheck.value > 5 * 60 * 1000) {
		lastCheck.value = now;
		const user = await auth.fetchMe();

		if (!user) return router.push("/login");
	}
});
 