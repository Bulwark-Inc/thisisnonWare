type HealthResponse = {
  status: string;
};

async function getBackendHealth(): Promise<string> {
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/api/v1/health`,
      {
        cache: "no-store",
      }
    );

    if (!response.ok) {
      return "unavailable";
    }

    const data: HealthResponse = await response.json();
    return data.status;
  } catch {
    return "unavailable";
  }
}

export default async function Home() {
  const backendStatus = await getBackendHealth();

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4">
      <h1 className="text-3xl font-bold">
        Cloud Run Fullstack Demo
      </h1>

      <p>
        Frontend Status: <strong>running</strong>
      </p>

      <p>
        Backend Status: <strong>{backendStatus}</strong>
      </p>
    </main>
  );
}