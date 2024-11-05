import os
import streamlit as st

st.markdown("""
<style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("AWS AirBnB Case Study")
st.caption("By Siddhant Joshi, Nakul Dighe, Dhruv Jadhav, Mihir Ginde, Sarvesh Lole, Darshan Kamat")

st.header("Understanding AWS and it's Scale")
st.markdown("**Amazon Web Services (AWS)** is a leading cloud computing platform that provides a range of services, such as computing, storage, and databases, to help businesses operate efficiently.")
st.image(os.path.join(os.getcwd(), "images", "scale-of-aws.png"))

st.header("Understanding AirBnB and it's Scale")
st.markdown("""
- **Platform Purpose**: Allows people to rent out homes or spare rooms to travelers.
- **Accommodation Variety**: Offers unique stays like apartments, houses, and treehouses globally.
- **Connection**: Links hosts with guests for diverse travel experiences.
- **Affordability**: Often provides more budget friendly options than hotels.
""")
st.image(os.path.join(os.getcwd(), "images", "scale-of-airbnb.png"))

st.header("AWS Services used by AirBnB")
st.markdown("""
- **Amazon EC2 (Elastic Compute Cloud)**: Supports Airbnb's application and search servers.\n
- **Elastic Load Balancer**: Distributes incoming traffic between multiple EC2 instances.\n
- **Amazon EMR (Elastic MapReduce)**: For processing and analyzing 50 GB of data daily.\n
- **Amazon S3 (Simple Storage Service)**: Stores backups and static files, including 10 TB of user images.\n
- **Amazon RDS (Relational Database Service)**: Hosts Airbnb's MySQL database with Multi-AZ deployment for data durability.\n
- **Amazon CloudWatch**: Monitors server resources.\n
- **AWS KMS (Key Management Service)**: Enhances security.\n
- **Amazon Kinesis**: Collects and processes real-time data for user interaction analysis.\n
- **Amazon OpenSearch Service**: Indexes and searches large datasets for log analysis and system health monitoring.\n
""")
st.caption(" Fun Fact - Airbnb was able to complete its entire database migration to Amazon RDS with only 15 minutes of downtime !!")

st.header("Optimizing costs by using savings plans")
st.markdown("""
- **Cost and Usage Report**:
  - Provides comprehensive visibility into spending, improving budget management and cost forecasting.
  - Benefit: Enhances budget control and forecasting.\n
- **Amazon S3 Intelligent-Tiering**:
  - Automatically transfers data between storage tiers based on usage patterns, ensuring payment only for actively used storage.
  - Benefit: Significantly reduces storage costs.\n
- **Savings Plans for Amazon EC2**:
  - Allows Airbnb to secure lower pricing by committing to a consistent usage amount for one or three years.
  - Benefit: Reduces compute costs.\n
- **Amazon OpenSearch Service**:
  - Utilizes UltraWarm storage for handling large volumes of log data, optimizing operational expenses related to data analytics.
  - Benefit: Achieves a 60% reduction in OpenSearch expenses.\n

Additionally, Airbnb reported achieving a **27% reduction in storage costs** as part of their cost optimization efforts.
""")

st.header("Tech stack")
st.markdown("""
- **Frontend**: HTML, CSS, JavaScript (React)\n
- **Backend**: Java, Ruby (Rails), Microservices\n
- **Database**: MySQL (hosted on AWS), Redis\n
- **DevOps**: Docker, Kubernetes\n
""")

st.header("AirBnB employees & customers about using AWS")
st.markdown("""
- **Toby Knaup (Engineer)**: "AWS listens to customers' needs... The low cost and simplicity made it a no-brainer to switch."\n
- **Ari Seigel (Senior Finance Manager)**: "Using Savings Plans has reduced our workload and driven cost savings."\n
- **Chris (Host)**: "We love traveling as locals, not tourists... We host to help guests live like locals."\n
- **Greg (Customer)**: "Needed a last-minute place on a road trip; Airbnb made it quick. Each stay has been clean, spacious, and better than most hotels."\n
""")

st.header("Thank You!")
