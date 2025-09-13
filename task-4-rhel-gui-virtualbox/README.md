# 🖥️ RHEL GUI with VirtualBox on EC2

## Introduction
This task showcases **nested virtualization on AWS**.  
You will launch a **RHEL GUI instance** on EC2, install VirtualBox inside it, and create a VM within the cloud-hosted environment.

Such setups are useful for testing multiple operating systems without additional hardware.

## Objectives
- Launch a RHEL GUI AMI in AWS.
- Install and configure VirtualBox.
- Create and manage a virtual machine inside EC2.

## Steps
1. Search for a RHEL GUI AMI in the AWS Marketplace.
2. Launch an EC2 instance from it with proper instance type (e.g., `t2.large`).
3. SSH into the instance and install VirtualBox.
4. Create and boot a new VM within VirtualBox.

## Blog Link
🔗 [Setting up RHEL GUI with VirtualBox](https://www.linkedin.com/posts/aman-kant-mahto_setting-up-rhel-gui-with-virtualbox-on-an-activity-7257462517260558336-04-n)

## Conclusion
Running VirtualBox inside EC2 allows experimentation with **multiple OS environments** while leveraging AWS’s elasticity.
