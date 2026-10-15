import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `
    <div class="container">
      <h1>Angular Docker Application</h1>
      <p>Angular 22 running successfully inside Docker!</p>
    </div>
  `
})
export class AppComponent {}