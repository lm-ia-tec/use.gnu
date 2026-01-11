<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>FitBella | Moda Fitness Feminina</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #fff;
            color: #333;
        }

        header {
            background: linear-gradient(135deg, #ff5f9e, #ff8ccf);
            color: white;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            font-size: 2.2rem;
        }

        header p {
            margin-top: 8px;
            font-size: 1.1rem;
        }

        nav {
            background: #f8f8f8;
            padding: 10px;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        nav a {
            text-decoration: none;
            color: #ff5f9e;
            font-weight: bold;
        }

        .banner {
            background-image: url("https://images.unsplash.com/photo-1594737625785-c26c66cfb8d8");
            background-size: cover;
            background-position: center;
            height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .banner h2 {
            background: rgba(0,0,0,0.6);
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
        }

        .container {
            padding: 40px 20px;
            max-width: 1200px;
            margin: auto;
        }

        .produtos {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
        }

        .produto {
            border: 1px solid #eee;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            transition: transform 0.3s;
        }

        .produto:hover {
            transform: scale(1.03);
        }

        .produto img {
            width: 100%;
            height: 250px;
            object-fit: cover;
        }

        .produto-info {
            padding: 15px;
            text-align: center;
        }

        .produto-info h3 {
            margin-bottom: 10px;
        }

        .produto-info p {
            color: #ff5f9e;
            font-weight: bold;
            font-size: 1.1rem;
        }

        .produto-info button {
            margin-top: 10px;
            padding: 10px 15px;
            border: none;
            background: #ff5f9e;
            color: white;
            border-radius: 20px;
            cursor: pointer;
        }

        .produto-info button:hover {
            background: #e84b8b;
        }

        footer {
            background: #222;
            color: #fff;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
        }

        footer p {
            font-size: 0.9rem;
        }
    </style>
</head>

<body>

<header>
    <h1>FitBella</h1>
    <p>Moda Fitness Feminina</p>
</header>

<nav>
    <a href="#">Início</a>
    <a href="#">Coleção</a>
    <a href="#">Promoções</a>
    <a href="#">Contato</a>
</nav>

<section class="banner">
    <h2>Estilo, conforto e performance</h2>
</section>

<section class="container">
    <h2 style="text-align:center; margin-bottom:30px;">Nossos Produtos</h2>

    <div class="produtos">
        <div class="produto">
            <img src="https://images.unsplash.com/photo-1599058917212-d750089bc07c" alt="Legging Fitness">
            <div class="produto-info">
                <h3>Legging Fitness</h3>
                <p>R$ 129,90</p>
                <button>Comprar</button>
            </div>
        </div>

        <div class="produto">
            <img src="https://images.unsplash.com/photo-1600180758890-6b94519a8ba6" alt="Top Fitness">
            <div class="produto-info">
                <h3>Top Fitness</h3>
                <p>R$ 79,90</p>
                <button>Comprar</button>
            </div>
        </div>

        <div class="produto">
            <img src="https://images.unsplash.com/photo-1617957742125-2cc7c7f6f7c1" alt="Conjunto Fitness">
            <div class="produto-info">
                <h3>Conjunto Fitness</h3>
                <p>R$ 189,90</p>
                <button>Comprar</button>
            </div>
        </div>
    </div>
</section>

<footer>
    <p>© 2026 FitBella - Moda Fitness Feminina</p>
    <p>Instagram | WhatsApp</p>
</footer>

</body>
</html>
