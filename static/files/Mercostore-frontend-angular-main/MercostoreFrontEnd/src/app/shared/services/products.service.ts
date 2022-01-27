import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  apiURL = 'http://localhost:3003/api/v1';
  constructor(private http:HttpClient) { }

  public getProdutos(page:number, rows:number ): Observable<any> {
   let token = localStorage.getItem('token');
    return this.http.get(`${this.apiURL}/produtos?PageNumber=${page}&RowspPage=${rows}`, {headers: {
      "Authorization": `Bearer ${token}`
    }} );
  }

  public getFiltroProdutos(IdVetex:number, NomeProduto:string, Marca:string, Departamento:string, Categoria:string, RowspPage:number, PageNumber: number, Seller:string ): Observable<any> {
    let token = localStorage.getItem('token');
     return this.http.get(`${this.apiURL}/filtroProdutos?IdVetex=${IdVetex}&NomeProduto=${NomeProduto}&Marca=${Marca}&Departamento=${Departamento}&Categoria=${Categoria}&RowspPage=${RowspPage}&PageNumber=${PageNumber}&Seller=${Seller}`,
      {headers: {
       "Authorization": `Bearer ${token}`
     }} );
   }
}
