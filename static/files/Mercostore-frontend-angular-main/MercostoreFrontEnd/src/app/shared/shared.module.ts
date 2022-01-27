import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatTableModule } from '@angular/material/table';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { MenuComponent } from './components/menu/menu.component'



@NgModule({
    declarations: [
    MenuComponent
  ],
    imports: [
      CommonModule,
      MatIconModule,
      MatCardModule,
      MatButtonModule,
      MatInputModule,
      MatSidenavModule,
      MatToolbarModule,
      MatListModule,
      MatTableModule,
      MatProgressSpinnerModule,
      ReactiveFormsModule,
      FormsModule,
      RouterModule
    ],
    exports: [
      CommonModule,
      MatIconModule,
      MatCardModule,
      MatButtonModule,
      MatInputModule,
      MatSidenavModule,
      MatToolbarModule,
      MatListModule,
      MatTableModule,
      MatProgressSpinnerModule,
      ReactiveFormsModule,
      FormsModule
    ],
    providers: [
    ]
  
  })
  export class SharedModule {
  }