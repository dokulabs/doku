import { DokuParams } from "@/lib/doku/common";
import { getAverageRequestDuration } from "@/lib/doku/request";
import {
	validateMetricsRequest,
	validateMetricsRequestType,
} from "@/utils/doku";

export async function POST(request: Request) {
	const formData = await request.json();
	const timeLimit = formData.timeLimit;

	const params: DokuParams = {
		timeLimit: {
			start: timeLimit.start,
			end: timeLimit.end,
		},
	};

	const validationParam = validateMetricsRequest(
		params,
		validateMetricsRequestType.AVERAGE_REQUEST_DURATION
	);

	if (!validationParam.success)
		return Response.json(validationParam.err, {
			status: 400,
		});

	const res: any = await getAverageRequestDuration(params);
	return Response.json(res);
}
