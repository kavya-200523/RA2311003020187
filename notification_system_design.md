# Notification System Architecture

## Introduction

This is an explanation of a simple backend notification system that will provide notifications about maintenance of vehicles.

The system enables the creation and viewing of notifications for vehicle maintenance. Such notifications can be created for activities like engine service, oil change, brake check, tyre check, or any other vehicle maintenance activity.

## Major Functionalities

- Create new notification
- See notifications list
- Store title, message, and status of notification
- Get API response in JSON format

## API Endpoints

### 1. Home API

Endpoint: GET /

Response: Backend server is running

### 2. Get Notifications

Endpoint: GET /notifications

This API returns the list of all notifications.

### 3. Add Notification

Endpoint: POST /notifications

Sample request body:

{
  "title": "Engine Service",
  "message": "Vehicle engine service is due tomorrow"
}

Sample response:

{
  "id": 2,
  "title": "Engine Service",
  "message": "Vehicle engine service is due tomorrow",
  "status": "pending"
}