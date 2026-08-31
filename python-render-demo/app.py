from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
import time
import os
import platform

app = FastAPI(
    title="Python Render Showcase App",
    description="A standalone Python web application ready for 1-click deployment on Render.com",
    version="1.0.0"
)

# Start time tracking for uptime calculation
START_TIME = time.time()

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serves a modern, interactive dashboard showcasing Python on Render."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Render Showcase</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-color: #0f172a;
                --card-bg: rgba(30, 41, 59, 0.7);
                --card-border: rgba(255, 255, 255, 0.1);
                --accent-blue: #38bdf8;
                --accent-purple: #c084fc;
                --accent-green: #4ade80;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
            }
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                font-family: 'Inter', sans-serif;
                background-color: var(--bg-color);
                background-image: 
                    radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.15) 0px, transparent 50%),
                    radial-gradient(at 100% 100%, rgba(192, 132, 252, 0.15) 0px, transparent 50%);
                color: var(--text-main);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 2rem 1rem;
            }
            .container {
                max-width: 900px;
                width: 100%;
            }
            header {
                text-align: center;
                margin-bottom: 2.5rem;
            }
            .badge {
                display: inline-block;
                background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(192, 132, 252, 0.2));
                border: 1px solid var(--accent-blue);
                color: var(--accent-blue);
                font-size: 0.85rem;
                font-weight: 600;
                padding: 0.35rem 1rem;
                border-radius: 9999px;
                margin-bottom: 1rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            h1 {
                font-size: 2.5rem;
                font-weight: 700;
                background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.75rem;
            }
            p.subtitle {
                color: var(--text-muted);
                font-size: 1.1rem;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
                margin-bottom: 2rem;
            }
            .card {
                background: var(--card-bg);
                backdrop-filter: blur(12px);
                border: 1px solid var(--card-border);
                border-radius: 1rem;
                padding: 1.5rem;
                transition: transform 0.2s ease, border-color 0.2s ease;
            }
            .card:hover {
                transform: translateY(-4px);
                border-color: rgba(56, 189, 248, 0.4);
            }
            .card h3 {
                font-size: 1.2rem;
                margin-bottom: 0.75rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            .card p {
                color: var(--text-muted);
                font-size: 0.95rem;
                line-height: 1.5;
                margin-bottom: 1.25rem;
            }
            .btn {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: linear-gradient(135deg, #0284c7, #2563eb);
                color: white;
                text-decoration: none;
                padding: 0.6rem 1.2rem;
                border-radius: 0.5rem;
                font-weight: 600;
                font-size: 0.9rem;
                border: none;
                cursor: pointer;
                transition: opacity 0.2s;
            }
            .btn:hover {
                opacity: 0.9;
            }
            .btn-outline {
                background: transparent;
                border: 1px solid var(--accent-purple);
                color: var(--accent-purple);
            }
            .btn-outline:hover {
                background: rgba(192, 132, 252, 0.1);
            }
            .status-box {
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid var(--card-border);
                border-radius: 0.75rem;
                padding: 1rem;
                font-family: 'Fira Code', monospace;
                font-size: 0.85rem;
                color: var(--accent-green);
                overflow-x: auto;
            }
            .live-indicator {
                display: inline-block;
                width: 10px;
                height: 10px;
                background-color: var(--accent-green);
                border-radius: 50%;
                box-shadow: 0 0 10px var(--accent-green);
                margin-right: 0.5rem;
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.4; transform: scale(1.2); }
                100% { opacity: 1; transform: scale(1); }
            }
            footer {
                text-align: center;
                color: var(--text-muted);
                font-size: 0.85rem;
                margin-top: 3rem;
                border-top: 1px solid var(--card-border);
                padding-top: 1.5rem;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <span class="badge"><span class="live-indicator"></span> 100% Pure Python Showcase</span>
                <h1>Python App on Render.com</h1>
                <p class="subtitle">Fast, lightweight web application ready to be deployed & hosted with a live Render URL.</p>
            </header>

            <div class="grid">
                <div class="card">
                    <h3>⚡ Interactive REST API</h3>
                    <p>Powered by FastAPI in pure Python. Explore live endpoints, interactive Swagger UI, and auto-generated docs.</p>
                    <a href="/docs" target="_blank" class="btn">Explore OpenAPI Docs</a>
                </div>

                <div class="card">
                    <h3>📊 Live Analytics Engine</h3>
                    <p>Test Python calculation logic on demand. Computes statistical distributions and summary metrics dynamically.</p>
                    <button onclick="fetchAnalytics()" class="btn btn-outline">Run Sample Calculation</button>
                </div>

                <div class="card">
                    <h3>🟢 System Status & Health</h3>
                    <p>Inspect server metrics, environment details, runtime platform, and service health check responses.</p>
                    <button onclick="fetchHealth()" class="btn btn-outline">Check Service Health</button>
                </div>
            </div>

            <div class="card">
                <h3>💻 Terminal Output</h3>
                <div id="output" class="status-box">Ready. Click any action above to invoke live Python endpoints.</div>
            </div>

            <footer>
                Built with Pure Python & FastAPI • Deployable to Render.com with a single click
            </footer>
        </div>

        <script>
            async function fetchHealth() {
                const out = document.getElementById('output');
                out.innerText = 'Fetching /api/health...';
                try {
                    const res = await fetch('/api/health');
                    const data = await res.json();
                    out.innerText = JSON.stringify(data, null, 2);
                } catch (e) {
                    out.innerText = 'Error fetching health data: ' + e;
                }
            }

            async function fetchAnalytics() {
                const out = document.getElementById('output');
                out.innerText = 'Calculating Python metrics via /api/analytics...';
                try {
                    const res = await fetch('/api/analytics?numbers=12,45,67,23,89,90,34,56,78,100');
                    const data = await res.json();
                    out.innerText = JSON.stringify(data, null, 2);
                } catch (e) {
                    out.innerText = 'Error fetching analytics: ' + e;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/api/health")
def health_check():
    """Health check endpoint providing runtime & system information."""
    uptime_seconds = round(time.time() - START_TIME, 2)
    return {
        "status": "healthy",
        "service": "Python Render Showcase",
        "uptime_seconds": uptime_seconds,
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "render_env": os.getenv("RENDER", "false")
    }


@app.get("/api/analytics")
def analytics(numbers: str = Query(default="10,20,30,40,50", description="Comma-separated numbers")):
    """Sample Python analytics endpoint processing numbers in pure Python."""
    try:
        num_list = [float(n.strip()) for n in numbers.split(",") if n.strip()]
        if not num_list:
            return JSONResponse(status_code=400, content={"error": "No valid numbers provided."})
        
        count = len(num_list)
        total = sum(num_list)
        mean = total / count
        sorted_nums = sorted(num_list)
        
        # Calculate median
        if count % 2 == 1:
            median = sorted_nums[count // 2]
        else:
            median = (sorted_nums[count // 2 - 1] + sorted_nums[count // 2]) / 2.0
            
        variance = sum((x - mean) ** 2 for x in num_list) / count
        std_dev = variance ** 0.5

        return {
            "input_numbers": num_list,
            "metrics": {
                "count": count,
                "sum": total,
                "mean": round(mean, 4),
                "median": round(median, 4),
                "min": min(num_list),
                "max": max(num_list),
                "std_dev": round(std_dev, 4)
            }
        }
    except ValueError:
        return JSONResponse(status_code=400, content={"error": "Invalid number format in query string."})
