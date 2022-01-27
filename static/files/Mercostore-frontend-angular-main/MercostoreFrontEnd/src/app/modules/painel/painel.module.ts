import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from '../../shared/shared.module';
import { PainelRoutingModule } from './painel-routing.module';
import { FlexLayoutModule } from "@angular/flex-layout";
import { InfiniteScrollModule } from 'ngx-infinite-scroll';
import { DashboardComponent } from './dashboard/dashboard.component';

@NgModule({
  declarations: [ 
  
    DashboardComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    PainelRoutingModule,
    FlexLayoutModule,
    InfiniteScrollModule
  ]
})
export class PainelModule { }