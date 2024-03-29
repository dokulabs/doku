import { RESTRICTED_API_KEY_DELETION_NAMES } from "@/lib/doku/common";

export function maskingKey(key: string) {
	return key.slice(0, 3) + "..." + key.slice(-3);
}

export function normalizeAPIKeys(
	params: Partial<{ api_key: string; name: string }>[] | null | undefined
) {
	if (params?.length)
		return params.map((p) => ({
			...p,
			api_key: maskingKey(p?.api_key || ""),
		}));
}
