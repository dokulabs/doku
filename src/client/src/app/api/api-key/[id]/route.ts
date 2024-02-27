import { deleteAPIKey } from "@/lib/doku/api-key";

export async function DELETE(_: Request, context: any) {
	const { id } = context.params;
	const [err, res] = await deleteAPIKey(id);
	if (err)
		return Response.json(err, {
			status: 400,
		});
	return Response.json(res);
}
