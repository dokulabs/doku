import StatCard from "@/components/(playground)/stat-card";
import { AreaChart, BarList, LineChart } from "@tremor/react";
import { useCallback, useEffect } from "react";
import { useFilter } from "../filter-context";
import useFetchWrapper from "@/utils/hooks/useFetchWrapper";
import Card from "@/components/common/card";
import { getChartColors } from "@/constants/chart-colors";

function TopModels() {
	const [filter] = useFilter();
	const { data, fireRequest, isFetched, isLoading } = useFetchWrapper();

	const fetchData = useCallback(async () => {
		fireRequest({
			body: JSON.stringify({
				timeLimit: filter.timeLimit,
			}),
			requestType: "POST",
			url: "/api/metrics/model/top",
			responseDataKey: "data",
		});
	}, [filter]);

	useEffect(() => {
		if (filter.timeLimit.start && filter.timeLimit.end) fetchData();
	}, [filter, fetchData]);

	const colors = getChartColors((data as any[])?.length || 0);

	const updatedData = ((data as any[]) || []).map((item, index) => ({
		name: item.model,
		value: item.model_count,
		target: item.total,
		color: colors[index],
	}));

	return (
		<Card containerClass="rounded-l-lg w-1/2 h-full" heading="Top models">
			{isLoading || !isFetched ? (
				<div className="flex w-full items-center justify-center h-40">
					Loading...
				</div>
			) : updatedData.length === 0 ? (
				<div className="flex w-full items-center justify-center h-40">
					No data available
				</div>
			) : (
				<BarList
					data={isLoading || !isFetched ? [] : updatedData}
					className="h-40 text-tertiary"
					showAnimation
				/>
			)}
		</Card>
	);
}

function ModelsPerTime() {
	const [filter] = useFilter();
	const { data, fireRequest, isFetched, isLoading } = useFetchWrapper();
	const fetchData = useCallback(async () => {
		fireRequest({
			body: JSON.stringify({
				timeLimit: filter.timeLimit,
			}),
			requestType: "POST",
			url: "/api/metrics/model/time",
			responseDataKey: "data",
		});
	}, [filter]);

	useEffect(() => {
		if (filter.timeLimit.start && filter.timeLimit.end) fetchData();
	}, [filter, fetchData]);

	const models: Set<string> = new Set();

	const updatedDataWithType = (((data || []) as any[]) || []).map((item) => {
		models.add(item.model);
		return {
			request_time: item.request_time,
			[item.model]: item.model_count,
		};
	});

	const modelsArr = Array.from(models);
	const colors = getChartColors(modelsArr.length);

	return (
		<Card
			containerClass="rounded-r-lg w-full h-full border-l-0"
			heading="Models per time"
		>
			<LineChart
				className="h-40"
				connectNulls
				colors={colors}
				data={isLoading || !isFetched ? [] : updatedDataWithType}
				index="request_time"
				categories={modelsArr}
				noDataText={
					isLoading || !isFetched ? "Loading ..." : "No data available"
				}
				showAnimation
			/>
		</Card>
	);
}

function TokensPerTime() {
	const [filter] = useFilter();
	const { data, fireRequest, isFetched, isLoading } = useFetchWrapper();
	const fetchData = useCallback(async () => {
		fireRequest({
			body: JSON.stringify({
				timeLimit: filter.timeLimit,
			}),
			requestType: "POST",
			url: "/api/metrics/token/time",
			responseDataKey: "data",
		});
	}, [filter]);

	useEffect(() => {
		if (filter.timeLimit.start && filter.timeLimit.end) fetchData();
	}, [filter, fetchData]);

	const updatedDataWithType = ((data || []) as any[]) || [];

	const colors = getChartColors(3);

	return (
		<Card
			containerClass="rounded-r-lg w-full h-full border-l-0"
			heading="Tokens usage"
		>
			<AreaChart
				className="h-4/5"
				colors={colors}
				data={isLoading || !isFetched ? [] : updatedDataWithType}
				index="request_time"
				categories={["totaltokens", "prompttokens", "completiontokens"]}
				yAxisWidth={40}
				noDataText={
					isLoading || !isFetched ? "Loading ..." : "No data available"
				}
				showAnimation
			/>
		</Card>
	);
}

function TokenCharts() {
	return (
		<div className="flex flex-col w-full gap-4">
			<div className="flex mb-4 w-full">
				<div className="flex flex-col w-1/4">
					<StatCard
						containerClass="rounded-tl-lg border-b-0 w-full text-xs"
						dataKey="total_tokens"
						extraParams={{ type: "prompt" }}
						heading="Avg prompt tokens / request"
						loadingClass="h-8 w-12"
						textClass="text-2xl"
						url="/api/metrics/token/request/average"
					/>
					<StatCard
						containerClass="rounded-bl-lg w-full text-xs"
						dataKey="total_tokens"
						extraParams={{ type: "completion" }}
						heading="Avg completion tokens / request"
						loadingClass="h-8 w-12"
						textClass="text-2xl"
						url="/api/metrics/token/request/average"
					/>
				</div>
				<TokensPerTime />
			</div>
			<div className="flex mb-4 w-full">
				<TopModels />
				<ModelsPerTime />
			</div>
		</div>
	);
}

export default TokenCharts;
