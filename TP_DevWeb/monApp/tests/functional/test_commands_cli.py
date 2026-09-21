from monApp.models import Auteur,Livre

def test_loaddb_command(runner,testapp):

    file = "monApp/data/data.yml"
    # Appel de la commande
    result = runner.invoke(args=["loaddb", file])

    # Vérification que la commande s’est exécutée correctement
    assert result.exit_code == 0

    # Vérification de la bonne alimentation
    with testapp.app_context():
        nbA = Auteur.query.count()
        assert nbA == 69
        nbL = Livre.query.count()
        assert nbL == 100