import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'Retail Store';
  prn = '23070122047';
  student = 'Arsh Ansari';
  products = [
    { name: 'Wireless Mouse', price: 799 },
    { name: 'USB-C Hub', price: 1499 },
    { name: 'Laptop Sleeve', price: 599 },
  ];
}
