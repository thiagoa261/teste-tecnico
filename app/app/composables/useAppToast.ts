export function useAppToast() {
	const toast = useToast();

	function toastSuccess(message: string) {
		toast.add({
			title: "Sucesso",
			description: message,
			icon: "i-lucide-check",
			color: "success",
		});
	}

	function toastError(message: string) {
		toast.add({
			title: "Sucesso",
			description: message,
			icon: "i-lucide-check",
			color: "error",
		});
	}

	return {
		toastSuccess,
		toastError,
	};
}
