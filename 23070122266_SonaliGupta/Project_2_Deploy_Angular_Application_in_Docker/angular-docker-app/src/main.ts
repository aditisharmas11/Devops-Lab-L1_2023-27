import { bootstrapApplication } from '@angular/platform-browser';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `
    <div style="text-align: center; font-family: Arial, sans-serif; margin-top: 60px;">
      <h1 style="color: #dd0031;">Angular Application Deployed in Docker Container</h1>
      <h3>DevOps Lab - Sonali Gupta (23070122266)</h3>
      <p style="font-size: 18px; color: #555;">Development & Production Multi-Stage Deployment Verified</p>
    </div>
  `
})
export class AppComponent {}

bootstrapApplication(AppComponent).catch(err => console.error(err));
