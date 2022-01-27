export class Produtos {
    constructor(
        public Categoria: string,
        public Departamento: string,
        public EAN: string,
        public Id: number,
        public IdVetex: number,
        public Marca: string,
        public NomeProduto: string,
        public PrecoSeller: number,
        public Seller: string,
        public BitMenor: boolean,    
    ) {}
}