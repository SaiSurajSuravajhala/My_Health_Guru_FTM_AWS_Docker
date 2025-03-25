# My Health Guru: AI Health Assistant 🩺

A cloud-deployed AI system that answers health queries using fine-tuned NLP models, built with modern DevOps practices.

## 🌟 Key Features
- Health-specific question answering
- Fine-tuned medical NLP model
- Scalable cloud deployment
- Containerized microservice architecture

## 🛠️ Development Stack
- **AI Core**: HuggingFace Transformers (GPT-2)
- **API Layer**: FastAPI REST endpoint
- **Infrastructure**: Docker containerization + AWS Fargate (serverless)
- **Monitoring**: AWS CloudWatch logs

## 🔄 Workflow Pipeline
1. **Model Training**  
   → Curated health FAQ dataset  
   → Optimized for medical terminology

2. **API Packaging**  
   → FastAPI prediction endpoint  
   → Docker image creation

3. **Cloud Deployment**  
   → AWS ECR for image registry  
   → ECS cluster with Fargate compute  
   → Public IP exposure on port 8000

## 🚨 Operational Notes
- Implemented auto-scaling via Fargate
- Security group configured for public access
- Cost-optimized resource allocation (0.5 vCPU/1GB RAM)
- Post-deployment cleanup to prevent cloud billing

## 📍 Maintenance Tips
1. Scale ECS tasks for traffic spikes
2. Monitor CloudWatch for API metrics
3. Retrain model with new health data
4. Implement API authentication layer

---
