import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProdutosRoutingModule } from './produtos-routing.module'

import { SharedModule } from '../../shared/shared.module';
import { ProductsComponent } from './products/products.component'
import { FlexLayoutModule } from "@angular/flex-layout";

import { InfiniteScrollModule } from 'ngx-infinite-scroll';

@NgModule({
  declarations: [ 

  
    ProductsComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    ProdutosRoutingModule,
    FlexLayoutModule,
    InfiniteScrollModule
  ]
})
export class ProdutosModule { }