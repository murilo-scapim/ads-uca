public class Carro {

    // atributos
    String placa;
    String marca;
    String modelo;
    String cor;
    int velocidade;
    int ano;

    // métodos
    public void acelerar(int novaVelocidade) {
        if (novaVelocidade > 0) {
            velocidade += novaVelocidade;
            System.out.println(modelo + " acelerou");
        } else {
            System.out.println("Informe uma velocidade válida!");
        }
    }
}
