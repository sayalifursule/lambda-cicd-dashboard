from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_PAGE = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>AWS CI/CD Automation Dashboard</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: white;
        }

        .navbar{
            width:100%;
            padding:20px 50px;
            background:#111827;
            display:flex;
            justify-content:space-between;
            align-items:center;
            box-shadow:0 2px 10px rgba(0,0,0,0.4);
        }

        .navbar h2{
            color:#38bdf8;
        }

        .status{
            background:#22c55e;
            padding:10px 20px;
            border-radius:20px;
            font-weight:bold;
        }

        .container{
            width:85%;
            margin:auto;
            padding-top:40px;
        }

        .hero{
            text-align:center;
            margin-bottom:50px;
        }

        .hero h1{
            font-size:50px;
            color:#38bdf8;
            margin-bottom:15px;
        }

        .hero p{
            font-size:20px;
            color:#cbd5e1;
        }

        .dashboard{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
            gap:25px;
        }

        .card{
            background:#1e293b;
            padding:30px;
            border-radius:15px;
            box-shadow:0 0 15px rgba(0,0,0,0.4);
            transition:0.3s;
        }

        .card:hover{
            transform:translateY(-5px);
        }

        .card h2{
            margin-bottom:20px;
            color:#38bdf8;
        }

        .card p{
            margin:12px 0;
            font-size:18px;
        }

        .success{
            color:#22c55e;
            font-weight:bold;
        }

        .services{
            margin-top:50px;
        }

        .services h2{
            margin-bottom:20px;
            color:#38bdf8;
        }

        .service-container{
            display:flex;
            flex-wrap:wrap;
            gap:20px;
        }

        .service-box{
            background:#334155;
            padding:18px 28px;
            border-radius:12px;
            font-weight:bold;
            transition:0.3s;
        }

        .service-box:hover{
            background:#475569;
            cursor:pointer;
        }

        .logs{
            margin-top:50px;
        }

        .logs h2{
            color:#38bdf8;
            margin-bottom:20px;
        }

        .log-box{
            background:black;
            color:#22c55e;
            padding:25px;
            border-radius:12px;
            font-family:monospace;
            line-height:1.8;
            overflow:auto;
        }

        footer{
            text-align:center;
            margin-top:60px;
            padding:20px;
            color:#94a3b8;
        }

    </style>

</head>

<body>

    <div class="navbar">
        <h2>☁ AWS DevOps Dashboard</h2>
        <div class="status">Pipeline Active</div>
    </div>

    <div class="container">

        <div class="hero">
            <h1>🚀 CI/CD Pipeline Automation</h1>
            <p>Serverless Deployment using AWS Lambda & CodePipeline</p>
        </div>

        <div class="dashboard">

            <div class="card">
                <h2>📌 Pipeline Details</h2>

                <p><strong>Pipeline Name:</strong> {{ pipeline_name }}</p>
                <p><strong>Status:</strong>
                    <span class="success">{{ status }}</span>
                </p>

                <p><strong>Trigger:</strong> {{ trigger }}</p>
                <p><strong>Repository:</strong> {{ repository }}</p>
                <p><strong>Deployment:</strong> {{ deployment }}</p>
            </div>

            <div class="card">
                <h2>📊 Deployment Stats</h2>

                <p><strong>Last Deployment:</strong> {{ last_build }}</p>
                <p><strong>Build Duration:</strong> 2 mins 10 sec</p>
                <p><strong>Total Deployments:</strong> 18</p>
                <p><strong>Success Rate:</strong> 98%</p>
            </div>

            <div class="card">
                <h2>⚡ Automation Workflow</h2>

                <p>GitHub Push</p>
                <p>⬇</p>
                <p>AWS Lambda Trigger</p>
                <p>⬇</p>
                <p>CodePipeline Execution</p>
                <p>⬇</p>
                <p>Automated Deployment</p>
            </div>

        </div>

        <div class="services">

            <h2>🛠 AWS Services Used</h2>

            <div class="service-container">

                <div class="service-box">AWS Lambda</div>
                <div class="service-box">AWS CodePipeline</div>
                <div class="service-box">AWS CodeBuild</div>
                <div class="service-box">Amazon S3</div>
                <div class="service-box">GitHub</div>
                <div class="service-box">IAM Roles</div>

            </div>

        </div>

        <div class="logs">

            <h2>📜 Deployment Logs</h2>

            <div class="log-box">

                [INFO] GitHub webhook received<br>
                [INFO] Lambda triggered successfully<br>
                [INFO] CodePipeline execution started<br>
                [INFO] Build process completed<br>
                [INFO] Deployment completed successfully<br>
                [SUCCESS] Application is live 🚀

            </div>

        </div>

    </div>

    <footer>
        Built with AWS Lambda, CodePipeline & Flask
    </footer>

</body>
</html>

"""

@app.route('/')
def home():

    deployment_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return render_template_string(
        HTML_PAGE,
        pipeline_name="LambdaCICDPipeline",
        status="SUCCESS",
        trigger="AWS Lambda",
        repository="GitHub",
        deployment="Fully Automated",
        last_build=deployment_time
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)