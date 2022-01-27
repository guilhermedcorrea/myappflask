import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { ProductsService } from '../../../shared/services/products.service'
import { Produtos } from 'src/app/shared/models/products.model';
@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})


export class ProductsComponent implements OnInit {
  public formularioFiltroProduto: FormGroup = new FormGroup({
    IdVetex: new FormControl(null),
    EAN: new FormControl(null),
    Produto: new FormControl(null),
    Marca: new FormControl(null),
    Departamento: new FormControl(null),
    Categoria: new FormControl(null),
    Seller: new FormControl(null)
  });

  private firstPage:number = 1

  displayedColumns = ['IdVetex', 'EAN', 'Produto', 'Marca', 'Departamento', 'Categoria', 'Seller', 'PrecoSeller', 'MenorPreco'];
  dataSource = new MatTableDataSource<Produtos>();
  public loginADM = false
  constructor(private productsService: ProductsService) { }

  ngOnInit(): void {
    if (localStorage.getItem('ADM') === 'true'){
      this.loginADM = true
    }else{
      this.loginADM = false
    }
    this.loadingProducts(this.firstPage);
  }

  public loadingProducts(page:number, row:number = 90):void{
    let itens = page === 1 ? []:this.dataSource.data
    this.productsService.getProdutos(page,row)
      .subscribe(res => {
        this.dataSource = new MatTableDataSource ([...itens, ...res.produtos])
      })
  }

  onScroll(){
    console.log('filtro')
    this.firstPage = this.firstPage + 1
    this.loadingFilterProducts(this.firstPage)
    /*
    if (this.formularioFiltroProduto.value){
      console.log('consulta normal')
      this.firstPage = this.firstPage + 1
      this.loadingProducts(this.firstPage)
    }else{
      console.log('filtro')
      this.firstPage = this.firstPage + 1
      this.loadingFilterProducts(this.firstPage)
    }*/
  }

  public loadingFilterProducts(page:number, row:number = 90):void{
    let IdVetex = this.formularioFiltroProduto.value.IdVetex || '';
    let Produto = this.formularioFiltroProduto.value.Produto || '';
    let Marca = this.formularioFiltroProduto.value.Marca || '';
    let Departamento = this.formularioFiltroProduto.value.Departamento || '';
    let Categoria = this.formularioFiltroProduto.value.Categoria || '';
    let Seller = this.formularioFiltroProduto.value.Seller || '';
    if (this.loginADM === true){
      Seller = this.formularioFiltroProduto.value.Seller || '';
    }else{
      Seller = ''
    }
    let itens = page === 1 ? []:this.dataSource.data
    this.productsService.getFiltroProdutos(IdVetex,Produto,Marca,Departamento,Categoria,row,page,Seller)
      .subscribe(res => {
        console.log(res)
        this.dataSource = new MatTableDataSource ([...itens, ...res.produtos])
      },
      erro => {
        console.log(erro)
      })
  }

  public cleanFilter():void{
    this.formularioFiltroProduto.setValue({IdVetex: null, EAN:null, Produto: null, Marca: null, Departamento: null, Categoria: null, Seller:null});
    this.loadingProducts(1)
    this.firstPage = 1
  }

}
