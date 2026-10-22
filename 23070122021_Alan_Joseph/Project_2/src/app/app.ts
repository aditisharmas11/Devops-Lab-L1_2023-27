import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <main>
      <h1>Angular running in Docker</h1>
      <p>Button clicks: {{ count() }}</p>
      <button (click)="increment()">Click me</button>
    </main>
  `,
  styles: [`
    main { font-family: sans-serif; text-align: center; margin-top: 3rem; }
    button { padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer; }
  `]
})
export class App {
  count = signal(0);

  increment() {
    this.count.update((c) => c + 1);
  }
}
