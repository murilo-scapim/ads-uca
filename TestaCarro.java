public class TestaCarro {

    static void main() {

        Carro carro = new Carro();
        carro.placa = "BKR123";
        carro.marca = "Hyundai";
        carro.modelo = "HB20";
        carro.cor = "Prata";
        carro.ano = 2019;
        carro.velocidade = 100;

        carro.acelerar(20);

        System.out.println(carro.placa);
        System.out.println(carro.marca);
        System.out.println(carro.modelo);
        System.out.println(carro.cor);
        System.out.println(carro.ano);
        System.out.println(carro.velocidade);
    }
}
